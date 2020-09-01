import React, { Component } from "react";
import { render } from "react-dom";
import './singleAsset.css'

class SingleAsset extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
        };
    }

    render() {
        return(
            <div className='singleAsset'>
                <h1>Single Asset</h1>
            </div>
        )
    }
}

export default SingleAsset