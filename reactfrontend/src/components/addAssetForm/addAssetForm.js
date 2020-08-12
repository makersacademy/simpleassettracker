import React, { Component } from "react";
import { render } from "react-dom";
import { Redirect } from 'react-router-dom';


class AddAssetForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      asset: {
        assetTag: '',
        assetType: '',
        createdBy: '',
      },
    }
    this.submitHandler = this.submitHandler.bind(this)
  }

  getUserToken() {
    const token = localStorage.getItem("token")
    console.log(token)
  }

  submitHandler(event) {
    event.preventDefault()
    console.log('this ran')
  }

  changeHandler(event, indentifier) {
    event.preventDefault()
    const oldData = {...this.state.asset}
    console.log(indentifier)
    console.log(oldData)
  }
  
  render() {

    return(
      <div>
        {this.getUserToken()}
        <h1>Add an Asset</h1>
        <form onSubmit={this.submitHandler}>
          <input inputtype='input' type="text" onChange={(event) => this.changeHandler(event, 'assetTag')} name="AssetTag" id="id_add_asset_tag" placeholder="Asset Tag"></input>
          <input inputtype='select' type="text" onChange={(event) => this.changeHandler(event, 'assetType')} name="AssetType" id="id_add_asset_type" placeholder="Select asset type"></input>
          <button className='submitButton' id="id_add_asset_submit" type="submit" value="submit">Add Asset</button>
        </form>
      </div>
    )
  }
}

export default AddAssetForm;