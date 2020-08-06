import React, { Component } from "react";
import { render } from "react-dom";
import axios from 'axios';

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

      handleDelete(asset_object) {
      fetch(`http://localhost:8000/assets/api/asset/${asset_object.id}`, {
        method: 'DELETE',
        headers: {
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
            <h1>Assets</h1>
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