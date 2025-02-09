import {Wrapper} from "./Wrapper";
import {useState} from "react";
import {useNavigate} from 'react-router-dom';

export const ProductsCreate = () => {
    const [name, setName] = useState('');
    const [price, setPrice] = useState('');
    const [quantity, setQuantity] = useState('');
    const navigate = useNavigate();
    const apiUrl = process.env.BACKEND_API_URL || "http://localhost:8080/";
    const submit = async e => {
        e.preventDefault();

        await fetch(`${apiUrl}products`, {
            method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({
                name, price, quantity
            })
        });

        await navigate(-1);
    }

    return <Wrapper>
        <form className="mt-3" onSubmit={submit}>
            <div className="form-floating pb-3">
                <input className="form-control" placeholder="Name"
                       onChange={e => setName(e.target.value)}
                />
                <label>Name</label>
            </div>

            <div className="form-floating pb-3">
                <input type="number" className="form-control" placeholder="Price"
                       onChange={e => setPrice(e.target.value)}
                />
                <label>Price</label>
            </div>

            <div className="form-floating pb-3">
                <input type="number" className="form-control" placeholder="Quantity"
                       onChange={e => setQuantity(e.target.value)}
                />
                <label>Quantity</label>
            </div>

            <button className="w-100 btn btn-lg btn-primary" type="submit">Submit</button>
        </form>
    </Wrapper>
}