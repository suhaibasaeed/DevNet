const search_button = document.getElementById('search');
const list = document.getElementById('list');
const page_element = document.getElementById('pagecontrol');

const per_page = 10;

search_button.addEventListener('click', function() {
	
	let url = buildUrl("1",per_page);
	
	fetchPage(url);

}, false);

function buildUrl(page, count){
	let base_url = 'https://api.discogs.com/artists/1/releases';
	let url = base_url + "?page=" + page + "&per_page=" + count;

	return(url);
}

function fetchPage(url){
	//Fetch the endpoint
	fetch(url).then(function(response){
		return response.json();
	}).then(function(data){
		console.log(data);

		//Add the releases to the HTML element
		ListReleases(data.releases);

		//Build the page control
		buildPageControl(data.pagination);

	}).catch(function(err){
		console.warn('Error: ', err);
	});
}

function ListReleases(releases){
	//Clear the list element
	list.innerHTML = "";

	releases.forEach(release => {
		let release_element = document.createElement('div');
		release_element.classList.add('release');

		let id_element = document.createElement('span');
		id_element.innerText = "Id: " + release.id;
		id_element.classList.add('releaseid');
		release_element.appendChild(id_element);

		let title_element = document.createElement('span');		
		title_element.innerText = "Title: " + release.title;
		id_element.classList.add('releasetitle');
		release_element.appendChild(title_element);
				
		list.appendChild(release_element);
	});

};

function buildPageControl(pagination){

	//Clear the pager control
	page_element.innerHTML = "";

	//Add the 'previous' button	
	let prev_element = document.createElement('button');
	prev_element.innerText = "<< Prev";
	prev_element.classList.add("navbutton")
	
	if(typeof pagination.urls.prev != "undefined"){		
		prev_element.addEventListener('click', function(){
			fetchPage(pagination.urls.prev);
		});
	}
	else {
		prev_element.disabled = true;
	}	

	page_element.appendChild(prev_element);

	//Add links for up to three prior pages
	//e.g <<Prev>> 1 ... 4  5  6  <7>  8  9  10 ... 17 <<Next>> 
	let currentPage = parseInt(pagination.page);		
	let pageCount = currentPage - 3;
	
	//Create a link for the first page
	if (currentPage > 1){
		let url = buildUrl("1",per_page);
		let link_element = document.createElement("span");
		link_element.classList.add('pageLink');
		link_element.innerText = "1";
		link_element.addEventListener('click', function(){
			fetchPage(url);
		});
		page_element.appendChild(link_element);
	}

	//Add an ellipses if needed
	if(pageCount>1){
		let elipses_element = document.createElement("span");
		elipses_element.innerText = '...';
		page_element.appendChild(elipses_element);
	}


	for(i=pageCount; i < currentPage; i++) {
		if(i > 1){
			let url = buildUrl(i,per_page);
			let link_element = document.createElement("span");
			link_element.classList.add('pageLink');
			link_element.innerText = i;
			link_element.addEventListener('click', function(){
				fetchPage(url);
			});
			page_element.appendChild(link_element);
		}
	}

	//Add a placeholder for current page
	let current_element = document.createElement("span");
	current_element.classList.add("currentLink");
	current_element.innerText = currentPage;
	page_element.appendChild(current_element);

	
	//Add links for up to three subsequent pages
	//e.g <<Prev>> 1 ... 4  5  6  <7>  8  9  10 ... 17 <<Next>> 
	let totalPages = parseInt(pagination.pages);
	pageCount = currentPage + 3;


	for(i=currentPage + 1; i <= pageCount; i++) {
		if (i < totalPages) {
			let url = buildUrl(i,per_page);
			let link_element = document.createElement("span");
			link_element.classList.add('pageLink');
			link_element.innerText = i;
			link_element.addEventListener('click', function(){
				fetchPage(url);
			});
			page_element.appendChild(link_element);
		}		
	}

	//Add ellipses if needed
	if(pageCount < totalPages){
		let elipses_element = document.createElement("span");
		elipses_element.innerText = '...';
		page_element.appendChild(elipses_element);
	}

	//Create a link for the last page
	if(currentPage < totalPages){
		url = buildUrl(pagination.pages,per_page);
		link_element = document.createElement("span");
		link_element.classList.add('pageLink');
		link_element.innerText = pagination.pages;
		link_element.addEventListener('click', function(){
			fetchPage(url);
		});
		page_element.appendChild(link_element);
	}

	//Add the 'next' button	
	let next_element = document.createElement('button');
	next_element.innerText = "Next >>";
	next_element.classList.add("navbutton")
	
	if(typeof pagination.urls.prev != "undefined"){		
		next_element.addEventListener('click', function(){
			fetchPage(pagination.urls.next);
		});
	}
	else {
		next_element.disabled = true;
	}	

	page_element.appendChild(next_element);
}