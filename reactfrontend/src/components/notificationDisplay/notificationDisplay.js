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
            notifications: [],
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
					return fetch("/notifications/api/notifications")
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
