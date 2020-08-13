import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom'
import AssetDisplay from './assetDisplay/assetDisplay'
import AddAssetForm from './addAssetForm/addAssetForm'

class App extends Component {

  render() {
    return (
      <div className="App">
          <Switch>
            <Route path='/assets/add' component={AddAssetForm} />
            <Route path='/assets' exact component={AssetDisplay} />
          </Switch>
      </div>
    );
  }
}

export default App;