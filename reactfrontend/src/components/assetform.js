import React, { Component } from "react";
import { render } from "react-dom";

class AssetForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            AssetForm: {
                AssetTag: "",
                DeviceType: "",
                CreatedBy: "",
            },
            loaded: false,
        };
    }
    handleSubmit = (event) => {
    event.preventDefault()

    const asset = {
      AssetTag: this.state.assetForm.assettag
      DeviceType: this.state.assetForm.devicetype
      CreatedBy: this.state.assetForm.createdby
    }


//    axios.post('/recipes.json', recipe)
//      .then(res => {
//        console.log(res)
//      })
//      .catch (err => {
//        console.log(err)
//      })
//  }
    }
    inputChangedHandler ="needs to be written"
    render(){
        return(
        <div>
        <form onSubmit={this.handleSubmit}>
                <Input inputtype='input' type="text" onChange={(event) => this.inputChangedHandler(event, 'AssetTag')} name="Asset Tag" placeholder="Recipe title"/>
                <Input inputtype='select' type="text" onChange={(event) => this.inputChangedHandler(event, 'DeviceType')} name="Device Type" className='add-select'/>
                <Input inputtype='input' type="text" onChange={(event) => this.inputChangedHandler(event, 'CreatedBy')} name="Created By" placeholder="Picture URL"/>
        </form>
        </div>
        )
    }



