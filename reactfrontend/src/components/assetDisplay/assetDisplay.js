import React, { Component } from "react";
import { render } from "react-dom";
import * as ReactBootStrap from 'react-bootstrap'
import './assetDisplay.css'

class AssetDisplay extends Component {
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
      <div className="table_container">
          <h1> Your Assets </h1>
          <div>
            <ReactBootStrap.Table class="table">
                <div>
                <thead>
                    <tr>
                        <th scope="col"> Asset Tag</th>
                        <th scope="col"> Device Type</th>
                        <th scope="col"> Created By</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.data.map(asset => {
                        return (
                            <tr key={asset.id} className="Asset-Hover">
                                <th scope="row">{asset.AssetTag}</th>
                                <td>{asset.DeviceType}</td>
                                <td>{asset.CreatedBy}</td>
                                <td><button id={"id_asset_delete_button_" + asset.id } onClick={() => this.handleDelete(asset)}>Delete</button></td>
                            </tr>
                        );
                    })}
                </tbody>
                </div>
            </ReactBootStrap.Table>
          </div>
      </div>
      );
    }
  }
  
  export default AssetDisplay;