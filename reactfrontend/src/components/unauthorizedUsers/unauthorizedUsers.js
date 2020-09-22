import React, { Component } from "react";
import { render } from "react-dom";
import * as ReactBootStrap from 'react-bootstrap'

class UnauthorizedUsersDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      unauthorizedusers: [],
      loaded: false,
      placeholder: "loading",
    };
  }

  componentDidMount() {
    fetch('/unauthorizedusers/api/unauthorizedusers')
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong..." };
          });
        }
      return response.json();
      })
      .then(data => {
        console.log(data)
        this.setState(() => {
          return {
            unauthorizedusers: data
          }
        });
      })
  }
  render() {
    return (
      <div className="table_container">
        <h1>Users Awaiting Authorization</h1>
        <ReactBootStrap.Table>
          <thead>
            <tr>
             <th>User ID</th>
            </tr>
          </thead>
          <tbody>
            {this.state.unauthorizedusers.map(user => {
              return(
                <tr key={user.id} className="user_row">
                  <td id="userid">{user.User}</td>
                </tr>
              )
            })}
          </tbody>
        </ReactBootStrap.Table>
        
      </div>
    )
  }
}

export default UnauthorizedUsersDisplay;