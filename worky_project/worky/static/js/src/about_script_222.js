import React, { useState } from 'react';
import ReactDOM from 'react-dom';

const PlusComponent = () => {
  const [openedPlus, setOpenedPlus] = useState(null);

  const togglePlus = (plusNumber) => {
    if (openedPlus === plusNumber) {
      // Toggle close if the same plus is clicked again
      setOpenedPlus(null);
    } else {
      // Open a new plus and close the previously opened one
      setOpenedPlus(plusNumber);
    }
  };

  const isPlusOpened = (plusNumber) => {
    return openedPlus === plusNumber;
  };

  const plus = <svg width="36" height="31" viewBox="0 0 36 31" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.602539" y="11.3789" width="34.6457" height="7.53125" rx="2" fill="white"/>
  <rect x="13.5942" y="30.207" width="30.125" height="8.66141" rx="2" transform="rotate(-90 13.5942 30.207)" fill="white"/>
  </svg>
  const minus = <svg width="36" height="9" viewBox="0 0 36 9" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.602539" y="0.535156" width="34.6457" height="7.53125" rx="2" fill="#F7992B"/>
  </svg>
  
  

  return (
    <div className="plus-container">
      <div
        onClick={() => togglePlus(1)}
        className={`plus-button ${isPlusOpened(1) ? 'clicked' : ''}`}
      >
        {isPlusOpened(1) ? minus : plus} <p id="our_mission_title">OUR MISSION</p> 
      </div>
      <div className={`text ${isPlusOpened(1) ? 'visible' : ''}`}>
        <p id="our_mission_text">Designing sustainable, high-performance buildings requires an integration 
            of architectural and engineered systems into a balanced design of sustainability…</p>
        <ul id="our_mission_list">
            <li>Based on your project, get only what’s needed</li>
            <li>Cost effective, to secure construction process</li>
            <li>Premium quality. We always get the best people</li>
        </ul>
      </div>

      <div
        onClick={() => togglePlus(2)}
        className={`plus-button ${isPlusOpened(2) ? 'clicked' : ''}`}
      >
        {isPlusOpened(2) ? minus : plus} <p id="our_vision_title">OUR VISION</p> 
      </div>
      <div className={`text ${isPlusOpened(2) ? 'visible' : ''}`}>
        <p id="our_vision_text">We are here to meet your demand and resolve architecture issues the most beneficial way for you. 
        Our skilled experts are able to resolve complex and unusual cases in the shortest time.</p>
        <ul id="our_vision_list">
            <li>Each case for us is unique</li>
            <li>People are our ultimate resource</li>
            <li>We take Visa, MasterCard, Discover and American Express</li>
        </ul>
      </div>

      <div
        onClick={() => togglePlus(3)}
        className={`plus-button ${isPlusOpened(3) ? 'clicked' : ''}`}
      >
        {isPlusOpened(3) ? minus : plus} <p id="our_values_title">OUR VALUES</p> 
      </div>
      <div className={`text ${isPlusOpened(3) ? 'visible' : ''}`}>
        <p id="our_values_text">Through this experience Warmhouse  has acquired a high level of expertise 
        in the design and realisation of high-profile and luxury schemes,
        always reducing the complexity.</p>
        <ul id="our_values_list">
            <li>Commercial</li>
            <li>Education & Campus</li>
            <li>Healthcare & Life Sciences</li>
        </ul>
      </div>
    </div>
  );
};

ReactDOM.render(<PlusComponent />, document.querySelector("#plus_block"))



