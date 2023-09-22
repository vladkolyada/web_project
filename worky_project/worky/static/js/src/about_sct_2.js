import React, { useState } from 'react';
import ReactDOM from 'react-dom';


const ChangeOurMissionComponent = () => {
    const [isClicked, setClicked] = useState(false);

    const handleClick = () => {
        setClicked(prevState => !prevState);
    }

    const our_mission_plus_c1 = <div id="our_mission_plus">
                        <svg onClick={handleClick} style={{ cursor: 'pointer' }} width="36" height="31" viewBox="0 0 36 31" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="0.602539" y="11.3789" width="34.6457" height="7.53125" rx="2" fill="white"/>
                            <rect x="13.5942" y="30.207" width="30.125" height="8.66141" rx="2" transform="rotate(-90 13.5942 30.207)" fill="white"/>
                        </svg>
                        <p id="our_mission_title">OUR MISSION</p>
                       </div>;  
                 
    const our_mission_minus_c2 = <div id="our_mission_minus">
                            <svg onClick={handleClick} style={{ cursor: 'pointer' }} width="36" height="9" viewBox="0 0 36 9" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="0.602539" y="0.535156" width="34.6457" height="7.53125" rx="2" fill="#F7992B"/>
                            </svg>
                            <p id="our_mission_title">OUR MISSION</p>
                        </div> 

    return (
        <div>
            {isClicked ? our_mission_plus_c1 : our_mission_minus_c2}
        </div>
    );
};

ReactDOM.render(<ChangeOurMissionComponent />, document.querySelector("#our_mission_plus_block"));

