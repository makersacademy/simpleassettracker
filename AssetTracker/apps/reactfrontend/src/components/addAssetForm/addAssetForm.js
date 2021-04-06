import React, { Component } from "react";
import './addAssetForm.css'

class AddAssetForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedAsset: '',
      asset: {
        assetTag: '',
        deviceType: '',
        deviceModel: '',
        createdBy: '',
        assetStatus: 'Ready',
        assetCondition: 'Good',
        serialNumber: null,
        year: null,
        hardDrive: null,
        screenSize: null,
        ram: null,
        imei: null,
        storage: null,
        colour: null,
      },
      messageType: '',
      company: '',
      showMessage: false,
      companyusers: '',
    }
    this.submitHandler = this.submitHandler.bind(this)
    this.changeHandler = this.changeHandler.bind(this)
    this.hideMessageHandler = this.hideMessageHandler.bind(this)
    this.selectAssetHandler = this.selectAssetHandler.bind(this)
  }

  componentDidMount() {
    const newData = {...this.state.asset}
    let newDataUser = {...newData["createdBy"]}
    newDataUser = window.django.user.user_id
    newData["createdBy"] = newDataUser
    this.setState({asset: newData})
    this.getCompanyID()
  }

  getCookie(name) {
    let nameEQ = name + "=";
    let ca = document.cookie.split(';');
    for(let i=0;i < ca.length;i++) {
      let c = ca[i];
      while (c.charAt(0)==' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }

  getCompanyID(){
    fetch('/companyusers/api/companyusers/'+ window.django.user.user_id)
    .then(response => {
      if (response.status > 400) {
        return this.setState(() => {
          return { placeholder: "Something went wrong!" };
        });
      }
    return response.json();
    })
    .then(data => {
      this.setState(() => {
        return {
          company: data.company
        }
      });
    });
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
        "asset_tag": this.state.asset.assetTag,
        "device_type": this.state.asset.deviceType,
        "device_model": this.state.asset.deviceModel,
        "created_by": this.state.asset.createdBy,
        "asset_status": this.state.asset.assetStatus,
        "serial_number": this.state.asset.serialNumber,
        "asset_condition": this.state.asset.assetCondition,
        "ram": this.state.asset.ram,
        "year": this.state.asset.year,
        "screen_size": this.state.asset.screenSize,
        "hard_drive": this.state.asset.hardDrive,
        "company": this.state.company,
        "imei": this.state.asset.imei,
        "storage": this.state.asset.storage,
        "colour": this.state.asset.colour,
      }),
    })
    .then(response => {
      if (response.ok) {
        this.setState({ showMessage: true, messageType: "successMessage", selectedAsset: "" }) 
        return response.json()
      } else {
        this.setState({ showMessage: true, messageType: "failMessage" })
        throw new Error('Something went wrong ...');
      }
      })
    .catch(error => (console.log(error)));
  }

  changeHandler(event, identifier) {
    event.preventDefault()
    const newData = {...this.state.asset}
    let newDataElement = {...newData[identifier]}
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

  select_device_type() {
    if (this.state.selectedAsset === 'laptop_form') {
      return 'Laptop'
    } else {
      return 'Mobile'
    }
  }

  selectAssetHandler(event) { 
    let newState = this.state
    newState.selectedAsset = event.target.value
    newState.asset.deviceType = this.select_device_type()
    this.setState(newState)
  }

  assetTagIsUnique() {
    fetch('/companyusers/api/companyusers/')
    .then(response => {
      if (response.status > 400) {
        return this.setState(() => {
          return { placeholder: "Something went wrong!" };
        });
      }
    return response.json();
    })
    .then(data => {
      const newArry = this.finalizeCompanyResponse(data)
      this.setState(() => {
        return {
          companyusers: newArry
        }
      });
      return fetch("api/asset")
    })
    .then(response => {
      if (response.status > 400) {
        return this.setState(() => {
          return { placeholder: "Something went wrong!" };
        });
      }
      return response.json();
    })
    .then(data => {
      const newArry = this.finalizeResponse(data)
      if (newArry.includes(this.state.assetTag)){
        return false
        } else {
        return true
        }
    });
  };

	finalizeCompanyResponse(data) {
		let newArray = data.map(x => x.user)
		return newArray
	}

	finalizeResponse(data) {
		let length = data.length
		let newArray = []
		for(let i=0; i < length; i++) {
      if ( this.state.companyusers.includes(data[i].Created_by) ) {
        newArray.push(data[i])
      }
		}
		return newArray
	}

  renderSelectedForm(param) {
    switch(param) {
      case 'laptop_form':
        return <form name="laptop_form" id="laptop_form" onSubmit={this.submitHandler}>
                <label className="asset_add_title" htmlFor="id_add_asset_tag">Asset Tag:</label>
                <input className="add_asset_input" inputtype='input' required type="text" onChange={(event) => this.changeHandler(event, 'assetTag')} name="assetTag" id="id_add_asset_tag"></input>
                <label className="asset_add_title" htmlFor="id_add_serial_number">Serial Number:</label>
                <input className="add_asset_input" inputtype='input' required type="text" onChange={(event) => this.changeHandler(event,'serialNumber')} name="serialNumber" id="id_add_serial_number"></input>
                <label className="asset_add_title" htmlFor="id_add_asset_model">Asset Model:</label>
                <select name="deviceModel" id="id_add_asset_model" required className="add_asset_input" onChange={(event) => this.changeHandler(event, 'deviceModel')}>
                  <option value="">Select model...</option>
                  <option value="Air">Air</option>
                  <option value="MacBook">MacBook</option>
                  <option value="Pro">Pro</option>
                </select>
                <label className="asset_add_title" htmlFor="id_add_asset_condition" >Asset Condition:</label>
                <select defaultValue='Good' name="assetCondition" id="id_add_asset_condition" className="add_asset_input" onChange={(event) => this.changeHandler(event, 'assetCondition')}>
                  <option value="Good">Good</option>
                  <option value="Bad">Bad</option>
                  <option value="Okay">Okay</option>
                  <option value="Broken">Broken</option>
                  <option value="New">New</option>
                </select>
                <label className="asset_add_title" htmlFor="id_add_asset_status" >Asset Status:</label>
                <select defaultValue='Ready' name="assetStatus" id="id_add_asset_status" className="add_asset_input" onChange={(event) => this.changeHandler(event, 'assetStatus')}>
                  <option value="Ready">Ready</option>
                  <option value="In Repair">In Repair</option>
                  <option value="Locked at the office">Locked at the office</option>
                  <option value="On Loan">On Loan</option>
                  <option value="Needs Resetting">Needs Resetting</option>
                  <option value="Extended Loan">Extended Loan</option>
                  <option value="Unknown">Unknown</option>
                  <option value="Lost">Lost</option>
                  <option value="Stolen">Stolen</option>
                  <option value="Unavailable">Unavailable</option>
                </select>
                <label className="asset_add_title" htmlFor="id_add_year">Year:</label>
                <select name="year" id="id_add_year" className="add_asset_input" onChange={(event) => this.changeHandler(event, 'year')}>
                  <option>Select year...</option>
                  <option value="2012">2012</option>
                  <option value="2013">2013</option>
                  <option value="2014">2014</option>
                  <option value="2015">2015</option>
                  <option value="2016">2016</option>
                  <option value="2017">2017</option>
                  <option value="2018">2018</option>
                  <option value="2019">2019</option>
                  <option value="2020">2020</option>
                  <option value="2021">2021</option>
                </select>
                <label className="asset_add_title" htmlFor="id_add_ram">Ram:</label>
                <select name="ram" id="id_add_ram" className="add_asset_input" onChange={(event) => this.changeHandler(event, 'ram')}>
                  <option>Select size...</option>
                  <option value="8GB">8GB</option>
                  <option value="16GB">16GB</option>
                  <option value="24GB">24GB</option>
                  <option value="32GB">32GB</option>
                </select>
                <label className="asset_add_title" htmlFor="id_add_hard_drive">Hard Drive:</label>
                <select name="hardDrive" id="id_add_hard_drive" className="add_asset_input" onChange={(event) => this.changeHandler(event, 'hardDrive')}>
                  <option>Select size...</option>
                  <option value="128GB">128GB</option>
                  <option value="256GB">256GB</option>
                  <option value="512GB">512GB</option>
                  <option value="1TB">1TB</option>
                </select>
                <label className="asset_add_title" htmlFor="id_add_screen_size">Screen Size:</label>
                <select name="screenSize" id="id_add_screen_size" className="add_asset_input" onChange={(event) => this.changeHandler(event, 'screenSize')}>
                  <option>Select size...</option>
                  <option value="12 inches">12 inches</option>
                  <option value="13 inches">13 inches</option>
                  <option value="15 inches">15 inches</option>
                  <option value="16 inches">16 inches</option>
                </select>
                <button className='btn btn-primary' id="id_add_asset_submit" style={{marginTop:"14px", clear:'both'}} type="submit" value="submit">Add Asset</button>
              </form>;
      case 'mobile_form':
        return <form name="mobile_form" id="mobile_form" onSubmit={this.submitHandler}>
                <label className="asset_add_title" htmlFor="id_add_asset_tag">Asset Tag:</label>
                <input className="add_asset_input" inputtype='input' required type="text" onChange={(event) => this.changeHandler(event, 'assetTag')} name="assetTag" id="id_add_asset_tag"></input>
                <label className="asset_add_title" htmlFor="id_add_imei">IMEI:</label>
                <input className="add_asset_input" inputtype='input' required type="text" onChange={(event) => this.changeHandler(event,'imei')} name="imei" id="id_add_imei"></input>
                <label className="asset_add_title" htmlFor="id_add_asset_model">Asset Model:</label>
                <input className="add_asset_input" inputtype='input' required type="text" onChange={(event) => this.changeHandler(event,'deviceModel')} name="deviceModel" id="id_add_asset_model"></input>
                <label className="asset_add_title" htmlFor="id_add_asset_condition" >Asset Condition:</label>
                <select defaultValue='Good' name="assetCondition" id="id_add_asset_condition" className="add_asset_input" onChange={(event) => this.changeHandler(event, 'assetCondition')}>
                  <option value="Good">Good</option>
                  <option value="Bad">Bad</option>
                  <option value="Okay">Okay</option>
                  <option value="Broken">Broken</option>
                  <option value="New">New</option>
                </select>
                <label className="asset_add_title" htmlFor="id_add_asset_status" >Asset Status:</label>
                <select defaultValue='Ready' name="assetStatus" id="id_add_asset_status" className="add_asset_input" onChange={(event) => this.changeHandler(event, 'assetStatus')}>
                  <option value="Ready">Ready</option>
                  <option value="In Repair">In Repair</option>
                  <option value="Locked at the office">Locked at the office</option>
                  <option value="On Loan">On Loan</option>
                  <option value="Needs Resetting">Needs Resetting</option>
                  <option value="Extended Loan">Extended Loan</option>
                  <option value="Unknown">Unknown</option>
                  <option value="Lost">Lost</option>
                  <option value="Stolen">Stolen</option>
                  <option value="Unavailable">Unavailable</option>
                </select>
                <label className="asset_add_title" htmlFor="id_add_storage">Storage:</label>
                <select name="storage" id="id_add_storage" required className="add_asset_input" onChange={(event) => this.changeHandler(event, 'storage')}>
                  <option value="">Select storage...</option>
                  <option value="64GB">64GB</option>
                  <option value="128GB">128GB</option>
                  <option value="256GB">256GB</option>
                </select>
                <label className="asset_add_title" htmlFor="id_add_colour">Colour:</label>
                <select name="colour" id="id_add_colour" required className="add_asset_input" onChange={(event) => this.changeHandler(event, 'colour')}>
                  <option value="">Select colour...</option>
                  <option value="White">White</option>
                  <option value="Space Grey">Space Grey</option>
                </select>
                <button className='btn btn-primary' id="id_add_asset_submit" style={{marginTop:"14px", clear:'both'}} type="submit" value="submit">Add Asset</button>
              </form>;
      default:
        return null;
    }
  }

  render() {
    console.log(this.state.companyusers)
    let message = null
    if(this.state.messageType == "successMessage" && this.state.showMessage == true) {
      message =
        <div>
          <div className='backdrop' onClick={() => this.hideMessageHandler()}></div>
          <div className='showMessage' onClick={() => this.hideMessageHandler()}>
            <h3>Successfully added</h3>
          </div>
        </div>
    } else if(this.state.messageType == "failMessage" && this.state.showMessage == true){
      message =
        <div>
          <div className='backdrop' onClick={() => this.hideMessageHandler()}></div>
          <div className='showMessage' onClick={() => this.hideMessageHandler()}>
            <h3>Failed to Add Asset - Asset Tag or Serial Number Not Unique</h3>
          </div>
        </div>
    }

    return(
      <div>
        {message}
        <div className="add_asset_container">
          <h1>Add an Asset</h1>
          <form id='id_choose_asset'>
            <select id='id_select_asset_type' value={this.state.selectedAsset} onChange={this.selectAssetHandler}>
              <option>Select an asset to add...</option>
              <option value='laptop_form'>Laptop</option>
              <option value='mobile_form'>Mobile</option>
            </select>
          </form>
          {this.renderSelectedForm(this.state.selectedAsset)}
        </div> 
      </div>
    )
  }
}

export default AddAssetForm;
