import React, { Component } from 'react';
import { render } from 'react-dom';
import * as ReactBootStrap from 'react-bootstrap';
import './dashboard.css';


class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      company: [],
      asset_count: null,
      laptop_count: null,
      mobile_count: null
    }
  }
  
  componentDidMount() {
    fetch(`/companyusers/api/companyusers/${window.django.user.user_id}`).then(response => {
      if (response.status > 400) {
        return this.setState(() => {
          return { placeholder: "Something went wrong!" };
        });
      }
    return response.json();
    })
    .then(data => {
      this.setState({ company: data.company });
      return fetch('/assets/api/asset')
    })
    .then(response => {
      if (response.status > 400) {
        return this.setState({ placeholder: "Something went wrong!" });
      }
      return response.json();
    })
    .then(assets => {
      let assets_counted = this.countAssets(assets);
      this.setState({ asset_count: assets_counted.asset_counter })
      this.setState({ laptop_count: assets_counted.laptop_counter })
      this.setState({ mobile_count: assets_counted.mobile_counter })
    });
  }
  
  countAssets(assets) {
    let laptop_counter = 0;
    let mobile_counter = 0;
    let asset_counter = 0
    assets.forEach((asset, idx) => {
      if (asset.device_type.toLowerCase() == 'laptop') {
        laptop_counter += 1
      } else { mobile_counter += 1 }
      asset_counter += 1
    })
    return { laptop_counter: laptop_counter, mobile_counter: mobile_counter, asset_counter: asset_counter }
  }
  
  messages() {
    
  }
  
  render() {
    
    if (this.state.asset_count == null) {
      return (
        <div>
          { /*this.messages()*/ }
          <div className='dashboard_container'>
            <h1 id='dashboard_title'>Your Dashboard</h1>
            <div className='dashboard_stat'>
            
              <div className='dashboard_stat_container_center'>
                <h4>Loading data...</h4>
              </div>
              
            </div>
          </div>
        </div>
      )
    } else {
      return (
        <div>
          { /*this.messages()*/ }
          <div className='dashboard_container'>
            <h1 id='dashboard_title'>Your Dashboard</h1>
            <div className='dashboard_stat'>
            
              <div className='dashboard_stat_container_left'>
                Total number of assets: { this.state.asset_count }
              </div>
              
              <div className='dashboard_stat_container_center'>
                Total number of laptops: { this.state.laptop_count }
              </div>
              
              <div className='dashboard_stat_container_right'>
                Total number of mobiles: { this.state.mobile_count }
              </div>
              
            </div>
          </div>
        </div>
      )
    }
  }
}

export default Dashboard;