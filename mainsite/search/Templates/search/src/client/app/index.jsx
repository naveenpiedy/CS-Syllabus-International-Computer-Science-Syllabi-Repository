import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  render () {
    return <div class="container mt-5">
          <div class="row">
              <div class="col-md-9">
                  <div class="form-group">
                    <label for="">Enter your Search</label>
                    <input type="text" class="form-control" name="search" id="search" aria-describedby="helpId" placeholder="" />
                    <small id="helpId" class="form-text text-muted">Help text</small>
                  </div>
              </div>
              <div class="col-md-3 align-self-center">
                  <button type="button" class="btn btn-dark">Search</button>
              </div>
          </div>
          <div>
            <div class="row">
                <div class='col-md-4'>
                    <div class="form-group">
                      <label for="professor">Professor</label>
                      <input type="text" class="form-control" name="professor" id="professor " aria-describedby="helpId" placeholder="" />
                      <small id="helpId" class="form-text text-muted">Help text</small>
                    </div>
                </div>
                <div class='col-md-4'>
                        <div class="form-group">
                          <label for="university">University</label>
                          <input type="text" class="form-control" name="university" id="university" aria-describedby="helpId" placeholder="" />
                          <small id="helpId" class="form-text text-muted">Help text</small>
                        </div>
                    </div>
            </div>
          </div>
      </div>
  }
}

ReactDOM.render(<App />, document.getElementById('app'));