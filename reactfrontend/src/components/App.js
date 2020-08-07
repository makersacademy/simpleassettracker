import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }
  
    componentDidMount() {
        fetch("api/asset")
            .then(response => {
            if (response.status > 400) {
                return this.setState(() => {
                return { placeholder: "Something went wrong!" };
                });
            }
            return response.json();
            })
            .then(data => {
                console.log(data)
                this.setState(() => {
                    return {
                    data,
                    loaded: true
                    };
                });
            });
    }

    getCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for(var i=0;i < ca.length;i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1,c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
        }
        return null;
    }


    handleDelete(asset_object) {
    fetch(`/assets/api/asset/${asset_object.id}`, {
        method: 'DELETE',
        headers: {
            "X-CSRFToken": this.getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
    })
    .then(() => {
        this.setState({data: this.state.data.filter(asset => asset_object.id !== asset.id)})
    });
    };


    render() {
      return (
          <div>


            <h1>Your Assets</h1>
            <ul>
            {this.state.data.map(asset => {
                return (
                <li key={asset.id}>
                    <button onClick={() => this.handleDelete(asset)}>Delete</button>
                    {asset.AssetTag} - {asset.DeviceType} - {asset.CreatedBy}

                </li>
                );
            })}
            </ul>
        </div>
      );
    }
  }
  
  export default App;
  
  const container = document.getElementById("app");
  render(<App />, container);