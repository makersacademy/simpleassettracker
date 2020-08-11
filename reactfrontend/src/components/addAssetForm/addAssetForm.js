import React, { Component } from "react";
import { render } from "react-dom";

class AddAssetForm extends Component {
  constructor(props) {
    super(props);
    this.state ={
      asset: {
        assetTag: '',
        assetType: '',
        createdBy: '',
      },
    }
  }

  getUserToken() {
    const token = localStorage.getItem("token")
    console.log(token)
  }
  
  render() {
    return(
      <div>
        {this.getUserToken()}
        <h1>Add an Asset</h1>
        <form onSubmit={this.handleSubmit}>
          <input inputtype='input' type="text" onChange={console.log('changing')} name="AssetTag" placeholder="Asset Tag"></input>
          <input inputtype='select' type="text" onChange={console.log('changing')} name="AssetType" placeholder="Select asset type"></input>
          <input inputtype='input' type="text" onChange={console.log('changing')} name="AssetTag" placeholder="Asset Tag"></input>
        </form>
      </div>
    )
  }
}

export default AddAssetForm;