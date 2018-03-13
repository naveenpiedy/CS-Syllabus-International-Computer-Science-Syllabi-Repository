import React from 'react';
import ReactDisqusComments from 'react-disqus-comments';
import {BrowserRouter as Router, Redirect} from 'react-router-dom'

export class Disquis extends React.Component {

  constructor(props){
    super(props);
    this.state = {comment:""}
    this.handleNewComment = this.handleNewComment.bind(this)
  }

  handleNewComment(commentt) {
    this.setState(comment= comment)
  }

  render() {
    console.log(this.props.unique_id + this.props.teachers_name + this.props.subjectName);
    return (
      <Router>
      <span>
      <Redirect push to={"/search/searching#!" +this.props.unique_id + this.props.teachers_name + this.props.subjectName} />
      <ReactDisqusComments
        shortname="localhost-GZDBeafv0k"
        identifier = {"http://127.0.0.1:8000/search/searching#!"+this.props.unique_id + this.props.teachers_name + this.props.subjectName}
        // title={this.props.subjectName}
        url= {"http://127.0.0.1:8000/search/searching#!"+this.props.unique_id + this.props.teachers_name + this.props.subjectName}
        //category_id= {this.props.unique_id}
        onNewComment={this.handleNewComment}/>
      </span>
      </Router>
    );
  }
}