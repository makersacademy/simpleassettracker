import React, { Component } from "react";
import { render } from "react-dom";
import * as ReactBootStrap from 'react-bootstrap'
import './assetDisplay.css'
import SingleAsset from '../singleAsset/singleAsset'

class AssetDisplay extends Component {
    constructor(props) {
        super(props);
        this.state = {
            companyusers: [],
            assets: [],
            loaded: false,
            placeholder: "Loading",           
            descending: false,
            showAsset: false,
            asset: null,
        };
		}

	
		componentDidMount() {
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
					data = this.finalizeCompanyResponse(data)
					this.setState(() => {
						return {
							companyusers: data
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
						data = this.finalizeResponse(data)
						this.setState(() => {
							return {
							assets: data,
							loaded: true
							};
						});
				});
			}
	
	finalizeCompanyResponse(data) {
		var newArray = data.map(x => x.User)
		return newArray
	}

	finalizeResponse(data) {
		var length = data.length
		var newArray = []
		for(var i=0; i < length; i++) {
				if ( this.state.companyusers.includes(data[i].CreatedBy) ) {
						newArray.push(data[i])
				}
		}
		return newArray
	}

	getCookie(name) {
		var nameEQ = name + "=";
		var ca = document.cookie.split(';');
		for(var i=0;i < ca.length;i++) {
			var c = ca[i];
			while (c.charAt(0)==' ') c = c.substring(1,c.length);
			if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
		}
		return null;
	}


	handleDelete(asset_object) {
		fetch(`/assets/api/asset/${asset_object.id}`, {
			method: 'DELETE',
			headers: {
					"X-CSRFToken": this.getCookie('csrftoken'),
					'Content-Type': 'application/json',
			},
		})
		.then(() => {
			this.setState({data: this.state.data.filter(asset => asset_object.id !== asset.id)})
		});
	};

	dynamicsort(property,order) {
		let sort_order = 1;
		if(order === "desc"){
			sort_order = -1;
		}
		return function (a, b){
			if(a[property] < b[property]){
				return -1 * sort_order;
			}else if(a[property] > b[property]){
				return 1 * sort_order;
			}else{
				return 0 * sort_order;
			}
		}
	}

	filterData(identifier) {
		const newData = [...this.state.data]
		let order = 'asc'
		if(this.state.descending === false) {
				order = 'desc'
				this.setState({ descending: true })
		} else {
				this.setState({ descending: false })
		}
		newData.sort(this.dynamicsort(identifier, order))

		this.setState({ data: newData })
	}

	showAsset(asset) {
        this.setState({ showAsset: true , asset: asset})
    }
    
	hideAsset() {
		this.setState({ showAsset: false })
	}

	render() {
		let arrow = null
		if(this.state.descending === false) {          
			arrow = <p style={{margin: '0 0 0 9px'}}>&#8593;</p>
		} else {
			arrow = <p style={{margin: '0 0 0 9px'}}>&#8595;</p>
		}

		let asset = null
		if(this.state.showAsset === true){
			asset = <SingleAsset asset={this.state.asset} hide={() => this.hideAsset()}/>
		}
		
		return (
		<div className="table_container">
			{asset}
			<h1 style={{marginLeft: '63px'}}>Your Assets</h1>
			<ReactBootStrap.Table>
				<thead>
					<tr>
						<th scope="col" className='delete_col'>{arrow}</th>
						<th scope="col" onClick={() => this.filterData('AssetTag')}>Asset Tag</th>
						<th scope="col" onClick={() => this.filterData('DeviceType')}>Device Type</th>
						<th scope="col" onClick={() => this.filterData('CreatedBy')} className='align_center'>Created By</th>
					</tr>
				</thead>
				<tbody>
					{this.state.assets.map(asset => {
						return (
							<tr key={asset.id} className="asset_row">
								<td className='delete_col'><button className='asset_delete_button' id={"id_asset_delete_button_" + asset.id } onClick={() => this.handleDelete(asset)}>X</button></td>
								<td id='tagid' onClick={() => this.showAsset(asset)} scope="row">{asset.AssetTag}</td>
								<td onClick={() => this.showAsset(asset)}>{asset.DeviceType}</td>
								<td onClick={() => this.showAsset(asset)} className='align_center'>{asset.CreatedBy}</td>
							</tr>
						);
					})}
				</tbody>
			</ReactBootStrap.Table>
		</div>
		);
	}
}
  
export default AssetDisplay;