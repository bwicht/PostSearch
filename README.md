# PostSearch

## Project Description

Our project aims to give an art interactive experience in pictures databases. A user is invited to strike a pose in front of a camera. ONce the picture is taken, we will try to match the users position with a similar one in the databased created, a displayed it on screen. Informations will be displayed about the matched painting or picture. The purpose is twofolds. First, it's an interactive browsing exeprience, that involve the visitor in the exhibition directly. With his actions, the image that it diplayes is different. It beaks linearity, observable in traditional art exhibitons. Second, the images presented would maybe never have been found otherwise than through this body interaction. We offer a new tool to experience srendipity.

## Conceptual References

### Serendipity
Serendipity is a concept related to randomness but with a positive outcome. The Oxford dictionary defines it as follows : *"The occurrence and development of events by chance in a happy or beneficial way"*. In the context of our interactive experience, the user can move from one painting to another, bringing images on the screen that he may never have seen before. During that sequence of events that he is experiencing as game, we hope that he may  also discover a painting that he has never have seen before. From a interactive playing experience, we also want to open the possibility to the user for an aesthetic exprience, and maybe, experiencing the sublime. Our experience then have two dimensions what could please the user : He could like the new way to interact with the dataset in a fun way, but also experience the sublime. We also find a new way to satisfy a user that would not just like to just mess around with the installation. 

|                                 | Experiences The Sublime | Doesn't Experience The Sublime |
| ------------------------------- | ----------------------- | ------------------------------ |
| Likes Playing Experience        | Had a good experience   | Had a good experience          |
| Doesn't Like Playing Experience | Had a good experience   | Had a bad experience           |

It is therefore important that the player could save his path that he followed or at least that he could have an way to keep a trace of the new discovery he made.



### Knowledge Vizualization
- Interconnections in different collections
### Aura
- Benjamin and the reproductibility of piece of art
- The digitalization of art images
- Technology, Aura and the authentic experience
### Museums
- Broken narratives
- Interactive exhibitions
- New Making of Meaning possibilities
### Interaction Design
- An artistic browsing experience
- A pipeline for future implementations and new interactive possibilites
- Body involvement as searching possibilities

### Ditigital Humanities
- The language of position
- Evolving he positions trough centuries
- Aby Warburg, Pathosformel and Morettti, a technical operationalization
- State of the art of applicable technology for projects
-  Computer Vision : Object detection and the nature of the object
- API, metadata and interoperability
- Ontologies
- Remix Culture

## Scalability

The first version of the project was focused on the development of an experience for Virtual Reality with the Oculus Rift. However we realized in the middle of the semester than VR may not be the best option in the context of paintings. We were doubtful that the Headset would enhance the experience. From that point, we decided to use a display to visualise the paintings. As we were using only simple controls to interact with the screen, it wasn't a problem no to use the Oculus one anymore. Any form of controllers, even rudimentary, would be enough for our user. 

Even if the Oculus quest can work without being linked to a computer, we still had to take a picture from the user in order to detect his position. For any form of camera, a kinect or a webcam, we were dependent of a tool that wasn't possible to integrate directly in the Oculus. We also had to analyze the picture taken, but that could easily be done remotley as well. From that point we could have either used a camera streaming the content to our Oculus or link the camera to the computer and analyse the pictures before sending everything to the headset. When finally going for a screen, an computer that host our application was then the way to go.

 From the beggining, the dataset that was retained to work with, was from Rijksmuseum. This Dataset consists approximately of 4300 photographs from their painting collection. We had to filter by hand the images that we wanted to retained for the experience. As we were focusing on poses, we had to remove all the pictures taht containes many paintings on a picture, landscapes and paintings where the group wa too big or the position unclear. After filtering the images, we had a dataset containing portraits and other representation from daily life. However we didn't have a lot of variation of positions in those paintings. We have the ability to match some positions but limited compared to the positions available. More data would have helped for more variation.

From those element, we thought our experience be for a single dataset and a single place of exhibition. However given the followed conditions :  the simplicity of the controller needed, the fact that every picture taken is analyzed before being matched with a database that could always be expended to enrich all the poses available in the database, leads to the the idea that our project can easily be implemented in different ways. It is then the core pipeline that is really important to define. Then that interactive tool can be implemented conceptually in VR, a phone app, on the web etc... All the project can be either used in a very lightweight version to implement on technologies that can't compute the images but have rapid internet connections. Or also be fully implemented locally as it is based on opensourced code and doesn't rely on a specific dataset. Our prject is then a demonstration on the Rijk Museum Dataset  that could also be implemented on images containing poses of any dataset. With that we go beyond [the Google Move Mirror](https://experiments.withgoogle.com/collection/ai/move-mirror/view) that is based on a dataset already constructed. From on a purely interactive experience, we browse dataset that have meaning for the context in which it is deployed ; a specifi Museum dataset, or private pictures.


## Roadmap

## General Roadmap
### Project Developement
- [x] First discussions to define project
- [x] Project presentation with core ideas and pipeline
- [x] Review of existing similar projects
- [x] Begin prototyping
- [x] Find a pose matching technology
- [x] Download Rijks Museum Dataset
- [x] Test different pose matching technologies
- [x] Prototype for User interface
- [x] Protoype for image segmentation
- [x] Second presentation with a Minimal Viable Product
- [x] Decision to focus on scalability
- [ ] Meeting to discuss about the next steps including:

###### Experience :
- [ ] Decisions about VR use
- [ ] Define  possible interactions for the user
- [ ] Decisions the users navigation possibilites after best match
- [ ] Bowsing Experience or just matching ?
- [ ] Define possible users controls
- [ ] Define incentives, what do we invite the person to do ?
- [ ] If headset, should we have a screen showing what happening
- [ ] If other technology, how could the user could 'save' his findings, or his match ?
- [ ] What do we espect as poses ?
- [ ] Wider range of poses or more precise poses ?

###### Developement :
- [ ] Decisions about the design of final UI, esthetic
- [ ] Decisions about the Database needed
- [ ] Decisions about the Metadata needed
- [ ] What technology will be used for final experience ?
- [ ] What is used to take a picture
- [ ] How the picture is transmitted to the UI ?
- [ ] Define incentives, what do we invite the person to do ?
- [ ] Should we interlink some API for a wider experience ?

###### Next :
- [ ] Catch-up with teacher after vacations
- [ ] Get an evolved prototype
- [ ] Test with real pictures
- [ ] Update this list


# PostSearch
