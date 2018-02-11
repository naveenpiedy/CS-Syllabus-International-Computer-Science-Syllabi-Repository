import React from 'react';
import ReactDOM from 'react-dom';
import {Body} from './body.jsx';

class App extends React.Component {


    constructor(props){
        super(props);
        this.state = {professor: "", university: "", subjectName: ""};
        this.sendProps = this.sendProps.bind(this);
    }

    sendProps(){
        let subjectName = document.getElementById("subjectName").value;
        let professor = document.getElementById("professor").value;
        let university = document.getElementById("university").value;

        this.setState({subjectName: subjectName, professor: professor, university: university})
    }

  render () {
    return <div class="container mt-5">
          <div class="row">
              <div class="col-md-9">
                  <div class="form-group">
                    <label for="">Enter the subject name to search</label>
                    <input type="text" class="form-control" name="subjectName" id="subjectName" aria-describedby="helpId" placeholder="" />
                    <small id="helpId" class="form-text text-muted">Help text</small>
                  </div>
              </div>
              <div class="col-md-3 align-self-center">
                  <button type="button" class="btn btn-dark" onClick={this.sendProps}>Search</button>
              </div>
          </div>
          <div>
            <div class="row">
                <div class='col-md-4'>
                    <div class="form-group">
                      <label for="professor">Professor</label>
                      <input type="text" class="form-control" name="professor" id="professor" aria-describedby="helpId" placeholder="" />
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
          <Body professor={this.state.professor} university = {this.state.university} subjectName = {this.state.subjectName} /> 
      </div>
  }
}

ReactDOM.render(<App />, document.getElementById('app'));