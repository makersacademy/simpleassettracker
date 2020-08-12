import React, { Component } from "react";
import { render } from "react-dom";
import { Redirect } from 'react-router-dom';


class AddAssetForm extends Component {
  constructor(props) {
    super(props);
    this.state ={
      redirect: null,
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

  handleSubmit(event) {
    event.preventDefault()
    this.setState({redirect: '/assets'})
    console.log('this ran')
  }
  
  render() {
    if (this.state.redirect) {
      return <Redirect to={this.state.redirect} />
    }

    return(
      <div>
        {this.getUserToken()}
        <h1>Add an Asset</h1>
        <form onSubmit={this.handleSubmit}>
          <input inputtype='input' type="text" onChange={console.log('changing')} name="AssetTag" id="id_add_asset_tag" placeholder="Asset Tag"></input>
          <input inputtype='select' type="text" onChange={console.log('changing')} name="AssetType" id="id_add_asset_type" placeholder="Select asset type"></input>
          <button className='submitButton' id="id_add_asset_submit" type="submit" value="submit">Add Asset</button>
        </form>
      </div>
    )
  }
}

export default AddAssetForm;