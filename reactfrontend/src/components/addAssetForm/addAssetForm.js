import React, { Component } from "react";
import './addAssetForm.css'

class AddAssetForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      asset: {
        assetTag: '',
        assetType: 'Laptop',
        createdBy: '',
        assetStatus: 'Ready',
        serialNumber: '',
      },
      showMessage: false,
    }
    this.submitHandler = this.submitHandler.bind(this)
    this.changeHandler = this.changeHandler.bind(this)
    this.hideMessageHandler = this.hideMessageHandler.bind(this)

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
            "CreatedBy": this.state.asset.createdBy,
            "AssetStatus": this.state.asset.assetStatus,
            "SerialNumber": this.state.asset.serialNumber
        },),
    })
    .then(response => {
        if (response.ok) {
          this.setState({ showMessage: true })
          $('#id_add_asset')[0].reset(); 
          return response.json()
        } else {
          throw new Error('Something went wrong ...');
        }
      })
    .catch(error => console.log(error))
  }

  changeHandler(event, identifier) {
    event.preventDefault()
    const newData = {...this.state.asset}
    let newDataElement = {...newData[identifier]}
    console.log(identifier)
    if (identifier === 'assetTag') {
      newDataElement = 'MA' + event.target.value
    } else {
      newDataElement = event.target.value
    }
    newData[identifier] = newDataElement
    this.setState({asset: newData})
  }

  hideMessageHandler() {
    this.setState({showMessage: false})
  }
  
  render() {
    let succesMessage = null
    if(this.state.showMessage) {
      succesMessage = 
        <div>
          <div className='backdrop' onClick={this.hideMessageHandler}></div>
          <div className='showMessage' onClick={this.hideMessageHandler}>
            <h3>Successfully added</h3>
          </div>
        </div>
    }

    return(
      <div>
        {succesMessage}
        <div className="add_asset_container">
            <h1>Add an Asset</h1>
            <form id='id_add_asset' onSubmit={this.submitHandler}>
            <label className="asset_add_title" for="id_add_asset_tag">Asset Tag:</label>
            <input className="add_asset_input" inputtype='input' required type="text" onChange={(event) => this.changeHandler(event, 'assetTag')} name="assetTag" id="id_add_asset_tag"></input>
            <label className="asset_add_title" for="id_add_asset_type" >Asset Type:</label>
            <select defaultValue='Laptop' name="assetType" id="id_add_asset_type" className="add_asset_input" onChange={(event) => this.changeHandler(event, 'assetType')}>
                <option value="Laptop">Laptop</option>
                <option value="Mobile">Mobile</option>
            </select>
            <label className="asset_add_serial_number" for="id_add_serial_number">Serial Number:</label>
            <input className="add_asset_input" inputtype='input' required type="text" onChange={(event) => this.changeHandler(event,'serialNumber')} name="serialNumber" id="id_add_serial_number"></input>
            <button className='btn btn-primary' id="id_add_asset_submit" style={{marginTop:"14px"}} type="submit" value="submit">Add Asset</button>
            </form>
        </div>
      </div>
    )
  }
}

export default AddAssetForm;