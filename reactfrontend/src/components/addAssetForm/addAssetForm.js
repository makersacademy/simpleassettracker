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
    this.changeHandler = this.changeHandler.bind(this)
  }

  componentDidMount() {
    const newData = {...this.state.asset}
    let newDataUser = {...newData["createdBy"]}
    newDataUser = window.django.user.user_id
    newData["createdBy"] = newDataUser
    this.setState({asset: newData})
  }

  submitHandler(event) {
    event.preventDefault()
    console.log('this ran')
  }

  changeHandler(event, identifier) {
    event.preventDefault()
    const newData = {...this.state.asset}
    let newDataElement = {...newData[identifier]}
    newDataElement = event.target.value
    newData[identifier] = newDataElement
    console.log(identifier)
    console.log(newData)
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