import React from 'react';
import ReactDOM from 'react-dom';

function Hello(props) {
    return (
        <h1>Hello! {props.name}.</h1>
    );
}

function App() {
    return (
        <div>
            <Hello name="Harry" />
            <Hello name="Ron" />
            <Hello name="Hermione" />
        </div>
    );
}


ReactDOM.render(<App />, document.querySelector('#root'));
