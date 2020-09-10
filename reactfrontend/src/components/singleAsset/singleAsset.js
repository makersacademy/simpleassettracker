import React, { Component } from "react";
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
        let tab1 = 'white'
        let tab2 = 'white'
        let tab3 = 'white'
        if(this.state.details === 'history'){
            details = <h1>History component</h1>
            tab1 = 'gray'
        } else if(this.state.details === 'details'){
            details = <h1>Details component</h1>
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
                            {console.log(this.props.asset)}
                            <h3>{this.props.asset.AssetTag}</h3>
                            <h3>{this.props.asset.DeviceType}</h3>
                        </div>
                    </div>
                    <div style={{ height: '60%'}}>
                        <div className='SingleAssetOptions'>
                            <h3 onClick={() => this.setState({ details: 'history' })} style={{backgroundColor: tab1}} className='SingleAssetOptionsTab' id='history-tab'>History</h3>
                            <h3 onClick={() => this.setState({ details: 'details' })} style={{backgroundColor: tab2}} className='SingleAssetOptionsTab' id='details-tab'>Details</h3>
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