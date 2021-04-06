import React, { Component } from "react";
import * as Papa from 'papaparse';
import './importcsv.css'

class uploadCSV extends React.Component {
  constructor() {
    super();
    this.state = {
      csvfile: undefined
    };
    this.handleChange = this.handleChange.bind(this);
    this.saveData = this.saveData.bind(this);
    this.importCSV = this.importCSV.bind(this);
  }

  handleChange(event) {
    console.log(event.target.files[0])
    this.setState({
      csvfile: event.target.files[0]
    });
    console.log(this.state.csvfile);
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
    console.log(data);
  }

  render() {
    console.log(this.state.csvfile);
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
      </div>
    );
  }
}

export default uploadCSV;
