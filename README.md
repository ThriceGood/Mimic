<div class="container">
 
         <h3>Mimic Docs</h3>
         <a href="http://localhost:5000/ui/" style="float: right;padding: 10px;">local index</a>
         <a href="http://localhost:5000/ui/insert" style="float: right;padding: 10px;">local insert</a>
         <a href="http://localhost:5000/ui/test" style="float: right;padding: 10px;">local test</a>
    <hr>
    <br>
    <br>

    <blockquote>
         <p><b>Mimic is a REST service mocker</b></p>
         <p>Mimic is a microservice designed to mock other microservices and REST APIs. It provides an interface to define mock endpoints, their desired request schema and their responses. A user makes a request to the mimic specifying the desired mock endpoint. Sent with this request is a payload containing the actual JSON that would be sent to the real service or API. The mimic compares the requests payload schema to the schema of the related mock endpoint, if it is a match, the desired response data is returned. All mimic endpoints can be interacted with via REST calls or by using the mimic wrapper. There is three aspects to Mimic, the mimic endpoints, the data endpoints and the user interface.</p>
    </blockquote>
    <br>
    <blockquote>
         <p><b>Installation</b></p>
        <p>Get the repo.</p>
        <p>Recommended: set up a virtual environment</p>
        <p>run: <code>$ python setup.py install</code></p>
        <p>start Mimic with: <code>$ mimic</code></p>
        <p>Mimic is now running on: localhost:5000</p>
        <p>You can get to the UI index with: localhost:5000/ui</p>
    </blockquote>
    <br>
    <blockquote>

         <p><b>Mimic endpoints</b></p>
         <p>Mimic (currently) has two endpoints for interacting with mock endpoints, a generic POST endpoint and a generic GET endpoint.</p>
         <br>
         <h5><b>POST</b></h5>
         <small>http://localhost:5000/mimic/post</small>
         <p>The generic post endpoint takes a JSON string that looks like this:</p>
         <pre>
             {
                "url": "url of desired endpoint",
                "tag": "a unique tag string",
                "payload": "JSON string representing the real request body"
             }
         </pre>
         <p>Mimic checks the database for an enpoint that matches the url and tag and if it finds a match returns it's schema and response payload. The request payload is compared to the endpoints schema and if it matches, the response payload is returned.</p>
         <p>In this way, you can post a request to the Mimic specifying the mock endpoint, have it validate your request payload and return your desired response payload.</p>
         <br>
         <h5><b>GET</b></h5>
         <small>http://localhost:5000/mimic/get</small>
         <p>The generic get endpoint is actually a post endpoint that takes JSON string that looks like this:</p>
         <pre>
             {
                "url": "url of desired endpoint",
                "tag": "a unique tag string",
                "query": "optional query string"
             }
         </pre>
         <p>It is called a get endpoint because it is mocking get endpoints. The endpoint with the desired tag and url is returned from the database and the request query string is compared to the endpoints schema, if it matches, the response payload is returned. If no query string is in the request then no comparison is made and the response is returned.</p>

    </blockquote>
    <br>
    <blockquote>
         <p><b>Data endpoints</b></p>
         <p>These endpoints are concerned with the CRUDing of your mock endpoints. The endpoint database looks like this:</p>
         <br>
         <table class="table">
        <tr>
            <th>id</th>
            <th>verb</th>
            <th>service</th>
            <th>url</th>
            <th>tag</th>
            <th>schema</th>
            <th>payload</th>
        </tr>
        <tr>
            <td>1</td>
            <td>POST</td>
            <td>some service</td>
            <td>/some/url/tail</td>
            <td>unique tag</td>
            <td>{"key1": "value1", "key2": "value2"}</td>
            <td>{"some big": "load of JSON data"}</td>
        </tr>
        <tr>
            <td>2</td>
            <td>GET</td>
            <td>some service</td>
            <td>/some/url/tail</td>
            <td>unique tag</td>
            <td>?key1=value1&key2=value2</td>
            <td>{"some big": "load of JSON data"}</td>
        </tr>
        </table>
        <br>
        <h5><b>Insert Endpoint</b></h5>
        <small>http://localhost/insert_endpoint</small>
        <p>This endpoint inserts a new mock endpoint and takes a JSON string that looks like this:</p>
        <pre>
            {
                "verb": "VERB",
                "service": "service name",
                "url": "url of endpoint",
                "tag": "unique tag",
                "schema": "expected request schema",
                "payload": "response payload to return",
            }
        </pre>
        <br>
        <h5><b>Update Endpoint</b></h5>
        <small>http://localhost/update_endpoint</small>
        <p>This endpoint updates a current mock endpoint and takes a JSON string that looks like this:</p>
        <pre>
            {
                "id": "id of endpoint",
                "verb": "VERB",
                "service": "service name",
                "url": "url of endpoint",
                "tag": "unique tag",
                "schema": "expected request schema",
                "payload": "response payload to return",
            }
        </pre>
        <br>
        <h5><b>Delete Endpoint</b></h5>
        <small>http://localhost/delete_endpoint/{id}</small>
        <p>This endpoint deletes a current mock endpoint and takes an endpoint id in the url</p>
    </blockquote>
    <br>
    <blockquote>
         <p><b>User Interface</b></p>
         <p>Mimic provides a user interface to CRUD your endpoints and test your endpoints, and also this docs page! The interfaces make AJAX calls to the endpoints and no endpoint requires the interface to be used.</p>
         <br>
         <h5><b>Index</b></h5>
        <small>http://localhost/ui/</small>
        <p>This endpoint returns an index page. It contains a table of all mock endpoints. Each endpoint row has a link for updating and deleting that endpoint.</p>
        <br>
         <h5><b>Insert</b></h5>
        <small>http://localhost/ui/inser_endpoint</small>
        <p>This endpoint returns an insert page. It contains a form that allows you to define new mock endpoints.</p>
        <br>
         <h5><b>Update</b></h5>
        <small>http://localhost/ui/update_endpoint/{id}</small>
        <p>This endpoint returns an update page. It contains a pre populated form that allows you to update the existing mock endpoint. It is accessed from the endpoint table in the index page.</p>
        <br>
        <h5><b>Test</b></h5>
        <small>http://localhost/ui/test</small>
        <p>This endpoint returns an endpoint test page. This page allows you to test a particular mock endpoint. You are provided with a form that allow you to enter the tag, url and payload (or query) for an endpoint and query it to see the response.</p>
        <br>
        <h5><b>Docs</b></h5>
        <small>http://localhost/ui/docs</small>
        <p>This endpoint returns this very Docs page!.</p>
    </blockquote>    
    <br>
    <blockquote>
        <p><b>The Mimic wrapper</b></p>
         <p>A wrapper is included to allow you to easily replace service wrapper calls with Mimic calls. A Mimic specific to a service can be instanciated with the service name as an argument. Alternatively a generic Mimic can be instanciated with no service name, although a service name will have to be passed to each call.</p>
         <h5><b>Usage examples:</b></h5>
         <pre>
            from wrapper.mimic_wrapper import Mimic

            # POST
            # generic mimic
            mimic = Mimic()
            url = '/service1/url'
            tag = 'my service1 call'
            payload = '{"key1": "value1", "key2": "value2"}'
            response = mimic.post(service='service1', url=url, tag=tag, payload=payload)
            print response

            # GET, query
            mimic = Mimic('service2')
            url = '/service2/url'
            tag = 'my service2 call'
            query = '?name=alarm'
            response = mimic.get(url=url, tag=tag, query=query)
            print response

            # GET, no query
            mimic = Mimic('service3')
            url = '/service3/url'
            tag = 'my service3 call'
            response = mimic.get(url=url, tag=tag)
            print response
         </pre>
    </blockquote>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <blockquote>
         <p>An optimistic mind-set finds dozens of possible solutions for every problem that the pessimist regards as incurable.</p>
         <small><cite>Robert Anton Wilson</cite></small>
    </blockquote>


      
     </div>