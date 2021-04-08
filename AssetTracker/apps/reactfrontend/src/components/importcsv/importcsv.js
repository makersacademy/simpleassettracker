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
      this.setState({error_message:"Sorry, that's not a valid CSV file!"});
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

  correctFieldInfoCheck(result) {
    result.data.forEach(obj => {
      this.state.fieldTitles.forEach(title => {
        if(!(title in obj)){
          this.setState({error_message: "Incorrect or Missing Field Name!"})
        } else if(obj[title] == ""){
          this.setState({error_message: "Missing Required Entry!"})
        }
      })
    })
  }

  saveData(result) {
    this.correctFieldInfoCheck(result)
    if (this.state.error_message !== null) return null

    let data = this.emptyStringCheck(result);
    let csrfToken = this.getCookie('csrftoken')

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
      <div className="importcsv_container">
        {message}
        <h1 id="csv_title">Import Assets</h1>
        <h3>Upload CSV Instructions</h3>
        <ul>
          <li>Download the CSV template file below</li>
          <li>Fill in your data
          <br />NB: Do not remove the header line or have empty lines</li>
          <li>Upload the updated file using the link above</li>
        </ul>
        <form id="csv_input_form">
          <label className="csv_label_title" htmlFor="csv_file">File:</label>
          <input
            className="csv_input"
            id="csv_file"
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
          <button
            className='btn btn-primary'
            id="upload_button"
            onClick={(event) => {event.preventDefault(); this.importCSV(); document.getElementById('csv-input-form').reset()}}>
            Upload 
          </button>
        </form>
        <p>{this.state.error_message}</p>
      </div>
    );
  }
}

export default uploadCSV;
