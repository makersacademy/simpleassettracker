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
          <Input inputtype='input' type="text" onChange={console.log('changing')} name="Asset Tag" placeholder="Asset Tag"></Input>
          <Input inputtype='select' type="text" onChange={console.log('changing')} name="Asset Type" placeholder="Select asset type"></Input>
          <Input inputtype='input' type="text" onChange={console.log('changing')} name="Asset Tag" placeholder="Asset Tag"></Input>
        </form>
      </div>
    )
  }
}

export default AddAssetForm;
  
  const container = document.getElementById("app");
  render(<AddAssetForm />, container);