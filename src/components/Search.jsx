import Form from 'react-bootstrap/Form';

function Search(){
    return (
        <div>
            <Form className="search-form">
                <Form.Label> Search</Form.Label>
                <Form.Control type="text" placeholder="Pokemon Name" />
                
            </Form>
        </div>
    );
}
export default Search;