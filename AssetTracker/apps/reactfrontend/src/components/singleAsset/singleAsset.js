import React, { Component } from "react";
import './singleAsset.css'

class SingleAsset extends Component {
  constructor(props) {
    super(props);
    this.state = {
     
      asset: {
        assetTag: '',
        deviceType: '',
        createdBy: '',
        assetStatus: '',
        serialNumber: '',
        assetCondition: ''
      }
    };
    console.log(props.asset.id)
  }

  componentDidMount() {
    this.setState({
      assetTag: this.props.asset.assetTag,
      deviceType: this.props.asset.deviceType,
      createdBy: this.props.asset.createdBy,
      assetStatus: this.props.asset.assetStatus,
      assetCondition: this.props.asset.assetCondition,
      serialNumber: this.props.asset.serialNumber
    })
  }

  changeHandler(event) {
    
    let itemChange = event.target.value
    this.setState({ asset: {assetStatus: itemChange}}, this.handleEdit);
    
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


  handleEdit(e) {
    event.preventDefault()

    console.log(this.assetStatus)
    let csrfToken = this.getCookie('csrftoken')
    console.log(this.state.asset.assetStatus)
     

      fetch(`api/asset/${this.props.asset.id}/`, {  
        method: "PATCH",  headers: {    
          "X-CSRFToken": csrfToken,   
          "Content-type": "application/json"  
        },  
        body: JSON.stringify({ 
          "asset_status": this.state.asset.assetStatus,  
        })}) .then(response => {    
          console.log(response.status);     
          return response.json();  })  
          .then(data => console.log(data));}

  render() {
    let details = null
    let tab1 = 'white'
    let tab2 = 'white'
    let tab3 = 'white'
    if(this.state.details === 'history'){
      details = <h1>History component</h1>
      tab1 = 'gray'
    } else if(this.state.details === 'details'){
      details = 
        <div>
          <h3>Screen Size: {this.props.asset.screen_size}</h3>
          <h3>Ram: {this.props.asset.ram}</h3>
          <h3>Year: {this.props.asset.year}</h3>
          <h3>Hard Drive: {this.props.asset.hard_drive}</h3>
          <h3>Condition: {this.props.asset.asset_condition}</h3>
        </div>
      tab2 = 'gray'
    } else if(this.state.details === 'notes'){
      details = <h1>Notes component</h1>
      tab3 = 'gray'
    } 

    return(
      <div className='singleAsset'>
        <div className='SingleAssetHeader'>
          <div style={{ height: '40%'}}>
            <img className='SingleAssetPicture' alt='picture' src='../../../static/frontend/img/laptop.png'/>
            <div className='SingleAssetSummary'>
              <h3>{this.props.asset.asset_tag}</h3>
              <h3>{this.props.asset.serial_number}</h3>
              <div>
                <select defaultValue={this.props.asset.asset_status} name="assetStatus" id="id_add_asset_status" className="change_assetstatus" onChange={(event) => this.changeHandler(event)}>
                  <option value="In Repair">In Repair</option>
                  <option value="Locked at the office">Locked at the office</option>
                  <option value="On Loan">On Loan</option>
                  <option value="Needs Resetting">Needs Resetting</option>
                  <option value="Extended Loan">Extended Loan</option>
                  <option value="Unknown">Unknown</option>
                  <option value="Lost">Lost</option>
                  <option value="Stolen">Stolen</option>
                  <option value="Unavailable">Unavailable</option>
                  <option value="Ready">Ready</option>
                </select>
              </div>
              <h3>{this.props.asset.device_type}</h3>
            </div>
          </div>
          <div style={{ height: '60%'}}>
            <div className='SingleAssetOptions'>
              <h3 onClick={() => this.setState({ details: 'details' })} style={{backgroundColor: tab2}} className='SingleAssetOptionsTab' id='details-tab'>Details</h3>
              <h3 onClick={() => this.setState({ details: 'history' })} style={{backgroundColor: tab1}} className='SingleAssetOptionsTab' id='history-tab'>History</h3>
              <h3 onClick={() => this.setState({ details: 'notes' })} style={{backgroundColor: tab3}} className='SingleAssetOptionsTab' id='notes-tab'>Notes</h3>
            </div>
            <div className='SingleAssetDetails'>
              {details}
            </div>
            <button className='SingleAssetButton' onClick={this.props.hide} id='single-asset-submit'>  ✔  </button>
          </div>
        </div>
      </div>
    )
  }
}

export default SingleAsset