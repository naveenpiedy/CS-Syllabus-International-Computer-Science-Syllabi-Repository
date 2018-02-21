import React from 'react';
import ReactDisqusComments from 'react-disqus-comments';

export class Disquis extends React.Component {

  constructor(props){
    super(props);
  }

  handleNewComment(comment) {
    console.log(comment.text);
  }

  render() {
    return (
      <ReactDisqusComments
        shortname="localhost-f7jqqi46tf"
        identifier={this.props.unique_id}
        //title="Example Thread"
        //url="http://www.example.com/example-thread"
        //category_id="123456"
        onNewComment={this.handleNewComment}/>
    );
  }
}