import React, { Component } from 'react';
import { render } from 'react-dom';
import * as ReactBootStrap from 'react-bootstrap';
import './dashboard.css';


class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      assets: {
        asset_count: 0,
        laptop_count: null,
        mobile_count: null
      }
    }
  }
  
  componentDidMount() {
    
  }
  
  messages() {
    
  }
  
  render() {
    
    if (this.state.assets.asset_count == null) {
      return null
    } else {
      return (
        <div>
          { /*this.messages()*/ }
          <div className='dashboard_container'>
            <h1 id='dashboard_title'>Dashboard</h1>
            <div className='dashboard_stat'>
            
              <div className='dashboard_stat_container_left'>
                Total number of assets: { this.state.assets.asset_count }
              </div>
              
              <div className='dashboard_stat_container_center'>
                Total number of assets: { this.state.assets.laptop_count }
              </div>
              
              <div className='dashboard_stat_container_right'>
                Total number of assets: { this.state.assets.mobile_count }
              </div>
              
            </div>
          </div>
        </div>
      )
    }
  }
}

export default Dashboard;