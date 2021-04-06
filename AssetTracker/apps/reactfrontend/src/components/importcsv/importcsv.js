import React, { Component } from "react";
import * as Papa from 'papaparse';
import './importcsv.css'

class uploadCSV extends React.Component {
  constructor() {
    super();
    this.state = {
      csvfile: undefined,
      company: null,
      error_message: null
    };
    this.handleChange = this.handleChange.bind(this);
    this.saveData = this.saveData.bind(this);
    this.importCSV = this.importCSV.bind(this);
  }

  componentDidMount() {
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
        this.setState({error_message:"Something went wrong!"})
      }
    return response.json();
    })
    .then(data => {
      this.setState({company:data.company});
    });
  }

  handleChange(event) {
    this.setState({
      csvfile: event.target.files[0]
    });
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

    data.forEach(asset => {
      fetch('/assets/api/asset/', {
        method: 'POST',
        headers: {
          "X-CSRFToken": csrfToken,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          ...asset,
          created_by:window.django.user.user_id,
          company:this.state.company
        }),
      })
      .then(response => {
        if (response.ok) { 
          return response.json()
        } else {
          throw new Error('Something went wrong ...');
        }
      })
      .catch(error => (console.log(error)));
    })
  }

  render() {
    return (
      <div className="App">
        <h2>Import CSV File!</h2>
        <input
          className="csv-input"
          type="file"
          ref={input => {
            this.filesInput = input;
          }}
          name="file"
          placeholder={null}
          onChange={this.handleChange}
        />
        <p />
        <button onClick={this.importCSV}> Upload now!</button>
        <p>{this.state.error_message}</p>
      </div>
    );
  }
}

export default uploadCSV;
