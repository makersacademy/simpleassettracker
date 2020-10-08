import React, { Component } from "react";
import { render } from "react-dom";
import * as ReactBootStrap from 'react-bootstrap'

class UnauthorizedUsersDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      unauthorizedusers: [],
      company: "",
      loaded: false,
      placeholder: "loading",
      showMessage: false,
      message: "",
    };
    this.hideMessageHandler = this.hideMessageHandler.bind(this)
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
        const newData = data.map(user => {
          this.setState({company: user.company})
          const extendUser = {...user.user, unauth_id: user.id}
          return extendUser
        })
        this.setState(() => {
          return {
            unauthorizedusers: newData
          }
        });
      })
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

  handleApprove(user_object) {
    fetch(`/approveuser/api/approveuser/${user_object.id}/`, {
			method: 'PATCH',
			headers: {
					"X-CSRFToken": this.getCookie('csrftoken'),
					'Content-Type': 'application/json',
			},
		})
		.then(() => {
      fetch(`/companyusers/api/companyusers/all`, {
        method: 'POST',
        headers: {
            "X-CSRFToken": this.getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "user": user_object.id,
            "company": this.state.company
        }),
      })
		})
		.then(() => {
      fetch(`/unauthorizedusers/api/unauthorizedusers/${user_object.unauth_id}/`, {
        method: 'DELETE',
        headers: {
            "X-CSRFToken": this.getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
      })
		})
		.then(() => {
			this.setState({unauthorizedusers: this.state.unauthorizedusers.filter(unauthorizedusers => user_object.id !== unauthorizedusers.id)})
			this.setState({showMessage: true})
			this.setState({message: "approve"})
		});

  }

  handleDeny(user_object){
    fetch(`/unauthorizedusers/api/unauthorizedusers/${user_object.unauth_id}/`, {
      method: 'DELETE',
      headers: {
        "X-CSRFToken": this.getCookie('csrftoken'),
        'Content-Type': 'application/json',
      },
    })
    .then(() => {
      fetch(`/approveuser/api/approveuser/${user_object.id}/`,{
        method: 'DELETE',
        headers: {
          "X-CSRFToken": this.getCookie('csrftoken'),
          'Content-Type': 'application/json',
        },
      })
    })
    .then(() => {
      this.setState({unauthorizedusers: this.state.unauthorizedusers.filter(unauthorizedusers => user_object.id !== unauthorizedusers.id)})
      this.setState({showMessage: true})
      this.setState({message: "deny"})
    });
  }

  hideMessageHandler() {
    this.setState({showMessage: false})
  }

  render() {
  let successMessage = null
    if(this.state.showMessage && this.state.message == "approve"){
    successMessage =
      <div>
        <div className='backdrop' onClick={this.hideMessageHandler}></div>
        <div className='showMessage' onClick={this.hideMessageHandler}>
          <h3>Successfully Approved</h3>
        </div>
      </div>
    }else if(this.state.showMessage && this.state.message == "deny"){
    successMessage =
      <div>
        <div className='backdrop' onClick={this.hideMessageHandler}></div>
        <div className='showMessage' onClick={this.hideMessageHandler}>
          <h3>Successfully Denied</h3>
        </div>
      </div>
    }
      return (
      <div>
        {successMessage}
        <div className="table_container">
          <h1>Unauthorized Users</h1>
          <ReactBootStrap.Table>
            <thead>
              <tr>
                <th scope="col">Username</th>
                <th scope="col">Email</th>
                <th scope="col">Approve/Deny</th>
              </tr>
            </thead>
            <tbody>
              {this.state.unauthorizedusers.map(user => {
                return (
                  <tr key={user.id} className="user_row">
                    <td>{user.username}</td>
                    <td>{user.email}</td>
                    <td><button class="btn btn-success" id={"id_user_approve_button_" + user.id } onClick={() => this.handleApprove(user)}>Approve</button>
                    <button class="btn btn-danger" id={"id_user_deny_button_" + user.id } onClick={() => this.handleDeny(user)}>Deny</button></td>
                  </tr>
                );
              })}
            </tbody>
          </ReactBootStrap.Table>
        </div>
      </div>
      );
    }
}

export default UnauthorizedUsersDisplay;
