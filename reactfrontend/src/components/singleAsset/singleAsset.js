import React, { Component } from "react";
import { render } from "react-dom";
import './singleAsset.css'

class SingleAsset extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            details: null,
        };
    }

    render() {
        let details = null
        if(this.state.details === 'history'){
            details = <h1>History</h1>
        } else if(this.state.details === 'details'){
            details = <h1>Details</h1>
        } else if(this.state.details === 'notes'){
            details = <h1>Notes</h1>
        } 


        return(
            <div className='singleAsset'>
                <div className='SingleAssetTitle'><h1>Single Asset</h1></div>
                <div className='SingleAssetHeader'>
                    <h1 className='SingleAssetPicture'>picture</h1>
                    <div className='SingleAssetSummary'>
                        {console.log(this.props.asset)}
                        <h3>{this.props.asset.AssetTag}</h3>
                        <h3>{this.props.asset.DeviceType}</h3>
                    </div>
                    <div className='SingleAssetOptions'>
                        <h1 onClick={() => this.setState({ details: 'notes' })} className='SingleAssetOptionsTab'>Notes</h1>
                        <h1 onClick={() => this.setState({ details: 'history' })}  className='SingleAssetOptionsTab'>History</h1>
                        <h1 onClick={() => this.setState({ details: 'details' })}  className='SingleAssetOptionsTab'>Details</h1>
                    </div>
                    <div className='SingleAssetDetails'>
                        {details}
                    </div>
                </div>
                <button className='SingleAssetButton' onClick={this.props.hide}>  ✔  </button>
            </div>
        )
    }
}

export default SingleAsset