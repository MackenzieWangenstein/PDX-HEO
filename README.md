# PDX-HEO
Portland Housing Emergency Outreach and Community Safety Web-app:

The goal of this project is to provide resources for Portland residents that are experiencing or  are vulnerable to experiencing issues relating to homelessness .

This project also has the goal to educate Portland residents about the extent of the housing crisis impacting the Portland and Portland metro area, as well as inform them on ways that they can take action to make an impact in their communities and make Portland a safer/better place for house-less residents.


Note: Although the target audience will eventually be mobile application users, the constraint of the development window for this class suggests that a web-app framework will be the best to quickly get out a prototype of the project functionality before the term ends.

OVERVIEW:


	-Allows users to identify their location to see nearby homeless shelters, shelters for domestic violence victims, woman and children.

	- Connects them with community resources that provide access to essential resources such as food, shelter, clothing, toiletries, etc

	-Has community boards/ forums where other people can connect and share community based  information relating to issues of poverty, homelessness, safety or other community concerns.

	- has a board members can post issues of safety concerns and report potental safety incidents to other PDX-HEO members. once this gets ported to a mobile framework we will introduce an interactive safety map a safety map where people can mark their locations and allow other mobile users to receive push notifications about safety concerns based upon their current location. In either case, it will be essential to post a message recommended users contact the proper safety channels to report the incidents and provide a link for users to easily contact non-emergency or emergancy services related to the incident type reported. (will suggest services such as portland respond and cheirs).





FEATURES:
	-Shelter finder
		-allows user to input address or location. Shows list of shelters that are sortable by location, type, etc

	-Resource/non-profit finder
			**UI: Interactive map with list of services
				-filter resources by:

					service-type:
						-housing resources
						-food/meal resources
						-essentials
						-education resources
						-safety
						-misc: counseling /legal advice/

					location:

				-community members can refer new organizations –
				-community members can rate organizations and provide comments and feedback

	-Community outreach
	-Forum/community board
				- members share and discuss community issues relating to poverty, housing, safety, and
				  any other community concerns.

	-Safety map
		    -members can pin their location and post message stating if they are experiencing safety concerns.

		     - users can mark their location and express safety concerns – the goal of this is to allow citizens to be able to post safety concerns about citizens (house-less or otherwise) without having to approach the resident to see if they need help. It will be essentially to provide a message and a link to encourage users to contact emrgancy/non-emergency services so they can also report the incident to the proper channels.


	-Connect members with non-emergency services
		-cheirs
		- Portland respond


	-testmonies  
	- about

IMPLEMENTATION:

	This project will start out as web-app with the goal to port the project to a mobile platform after the course has ended. We are still exploring which programming languages this application will be built with but we will be using docker-containers as our container platform.

	This project will maintain a database of the businesses/services that we will use in our shelter/resource finder. Exploring sql vs postgress.


MOTIVATION:

	Resources for house-less residents:

		- Cell phones can be a life-line for house-less residents and surveys suggest that many house-less residents have easy access to smart-phones. The goal of this project is to make it as 	simple and as user-friendly as possible for vulnerable residents to quickly find and access 	essential resources they need.

	Resources for concerned citizens:

		-As someone who spends a lot of time walking around downtown portland,  I have  encountered many situations where a house-less resident seemed to need help but wasn’t having a medical emergency. I was unsure of what the best way to help was at the moment because of a fear of escalating the situation further for the person by contacting the police. There are non-profit organizations in Portland that exist to serve this purpose but I was not aware of that at the time. The goal of this project is to make it easy for residents to take the appropriate action to best help people while being ability to feel confident that their decision to help fits on.




TEAM MEMBER:

Leading Contributers:
	- Mackenzie Wangenstein
	- Andy Mayer
	- Chitradevi Maruthavanan
	

Week 3 Report:
       - Current Project status:
             Database complete and website layout has been established. Currently the project is in the process of getting a Rest API setup using the Django REST Framework. The next steps for the project is to introduce javascript and css to the project so we can start fine tuning the look of the website. Back end logic is still needed to introduce the features that we are looking to implement such as the resource finder, the testimonies page, and if time permits a community board. If time permits we would like to create an android version of this app and introduce an interactive safety map where users can pinpoint their location and alert others of nearby safety conerns and hazards. This is where we will introduce the safety part of the name Portland Housing Emergancy Outreach and Safety.
       - Challenges:
           - Project Management: We found it challenging to create an assign issues for the beginning of the project while we were trying to set up the base structure of the application because we were all new to building a web app and using the django framework. Now that we have the database setup and the structure inplace to create webviews, it has been easier to come up with ideas of the work that needs to be done.
	   - Project structure/organization challenges need to addressed because of naming conventions used when first drafting the project.
