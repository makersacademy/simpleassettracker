import React, { Component } from "react";
import { render } from "react-dom";
import { Redirect } from 'react-router-dom';
import axios from "../../../axiosAsset";


class AddAssetForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      asset: {
        assetTag: '',
        assetType: '',
        createdBy: '',
      },
      placeholder: ''
    }
    this.submitHandler = this.submitHandler.bind(this)
    this.changeHandler = this.changeHandler.bind(this)
  }

  componentDidMount() {
    const newData = {...this.state.asset}
    let newDataUser = {...newData["createdBy"]}
    newDataUser = window.django.user.user_id
    newData["createdBy"] = newDataUser
    this.setState({asset: newData})
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

  submitHandler(event) {
    event.preventDefault()
    let csrfToken = this.getCookie('csrftoken')

    fetch('api/asset/', {
        method: 'POST',
        headers: {
            "X-CSRFToken": csrfToken,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "AssetTag": this.state.asset.assetTag,
            "DeviceType": this.state.asset.assetType,
            "CreatedBy": this.state.asset.createdBy
        },),
    })
    .then(response => response.json())
  }

  changeHandler(event, identifier) {
    event.preventDefault()
    const newData = {...this.state.asset}
    let newDataElement = {...newData[identifier]}
    newDataElement = event.target.value
    newData[identifier] = newDataElement
    this.setState({asset: newData})
  }
  
  render() {

    return(
      <div>
        <h1>Add an Asset</h1>
        <form onSubmit={this.submitHandler}>
          <input inputtype='input' type="text" onChange={(event) => this.changeHandler(event, 'assetTag')} name="assetTag" id="id_add_asset_tag" placeholder="Asset Tag"></input>
          <input inputtype='select' type="text" onChange={(event) => this.changeHandler(event, 'assetType')} name="assetType" id="id_add_asset_type" placeholder="Select asset type"></input>
          <button className='submitButton' id="id_add_asset_submit" type="submit" value="submit">Add Asset</button>
        </form>
      </div>
    )
  }
}

export default AddAssetForm;