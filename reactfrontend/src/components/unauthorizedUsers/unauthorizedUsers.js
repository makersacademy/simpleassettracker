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
        const newdata = data.map(user => {
          return user.User
        })
        console.log(newdata)
        this.setState(() => {
          return {
            unauthorizedusers: newdata
          }
        });
      })
  }

  render() {
      return (
      <div className="table_container">
        <h1 style={{marginLeft: '63px'}}>Unauthorized Users</h1>
        <ReactBootStrap.Table>
          <thead>
            <tr>
              <th scope="col">User ID</th>
              <th scope="col">Username</th>
              <th scope="col">Email</th>
            </tr>
          </thead>
          <tbody>
            {this.state.unauthorizedusers.map(user => {
              return (
                <tr key={user.id} className="user_row">
                  <td>{user.id}</td>
                  <td>{user.username}</td>
                  <td>{user.email}</td>
                </tr>
              );
            })}
          </tbody>
        </ReactBootStrap.Table>
      </div>
      );
    }
}

export default UnauthorizedUsersDisplay;
