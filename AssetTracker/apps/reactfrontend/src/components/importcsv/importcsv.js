import React, { Component } from "react";
import * as Papa from 'papaparse';
import './importcsv.css'

class uploadCSV extends React.Component {
  constructor() {
    super();
    this.state = {
      csvfile: undefined,
      company: null,
      error_message: null,
      messageType: '',
      showMessage: false,
      fieldTitles: ["asset_tag", "device_type", "device_model", "asset_status", "asset_condition"]
    };
    this.handleChange = this.handleChange.bind(this);
    this.saveData = this.saveData.bind(this);
    this.importCSV = this.importCSV.bind(this);
    this.hideMessageHandler = this.hideMessageHandler.bind(this);
  }

  componentDidMount() {
    this.getCompanyID()
  }

  hideMessageHandler() {
    this.setState({showMessage: false})
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
        this.setState({error_message:"Something went wrong!"})
      }
    return response.json();
    })
    .then(data => {
      this.setState({company:data.company});
    });
  }

  handleChange(event) {
    this.setState({error_message: null})
    if (event.target.files[0].type !== "text/csv") {
      this.setState({error_message:"Sorry, thats not a valid CSV file!"});
    }else{
      this.setState({csvfile: event.target.files[0]});
    }
  };

  importCSV() {
    const { csvfile } = this.state;
    Papa.parse(csvfile, {
      complete: this.saveData,
      header: true
    });
  };

  emptyStringCheck(result) {
    let newDataArray = []
    result.data.forEach(item => {
      let newData = {};
      Object.entries(item).forEach(keyPairValue => {
        if(keyPairValue[1] == ""){
          keyPairValue[1] = null
        }
        newData = {...newData, [keyPairValue[0]]:keyPairValue[1]}
      });
      newDataArray.push(newData)
    });
    return newDataArray
  }

  saveData(result) {
    let data = this.emptyStringCheck(result);
    let csrfToken = this.getCookie('csrftoken')
    let status = data.forEach(obj => {
      this.state.fieldTitles.forEach(title => {
        if(!(title in obj)){
          this.setState({error_message: "Missing Field!"})
        }
        if(obj[title] == null){
          this.setState({error_message: "Null Entry!"})
        }
      })
    })
    if (this.state.error_message !== null){
      return null
    }
    data.forEach(asset => {
      fetch('/assets/api/asset/', {
        method: 'POST',
        headers: {
          "X-CSRFToken": csrfToken,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          ...asset,
          created_by:parseInt(window.django.user.user_id),
          company:this.state.company
        }),
      })
      .then(response => {
        if (response.ok) {
          this.setState({ showMessage: true, messageType: "successMessage"})
          return response.json()
        } else {
          this.setState({ showMessage: true, messageType: "failMessage"})
          throw new Error('Something went wrong ...');
        }
      })
      .catch(error => (console.log(error)));
    })
    this.setState({ csvfile: null });
  }

  render() {

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

    return (
      <div className="App">
        {message}
        <h2>Import CSV File!</h2>
        <form id="csv-input-form">
          <input
            className="csv-input"
            type="file"
            accept=".csv"
            ref={input => {
              this.filesInput = input;
            }}
            name="file"
            placeholder={null}
            onChange={this.handleChange}
          />
          <p />
          <button onClick={(event) => {event.preventDefault(); this.importCSV(); document.getElementById('csv-input-form').reset()}}> Upload now!</button>
        </form>
        <p>{this.state.error_message}</p>
      </div>
    );
  }
}

export default uploadCSV;
