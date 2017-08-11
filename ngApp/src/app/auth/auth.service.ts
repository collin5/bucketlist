import { Injectable } from '@angular/core';
import { Http, Response, URLSearchParams } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/do';

@Injectable()
export class AuthService{
    constructor( private _http: Http ){}

    getToken(username: string, passphrase: string): Observable<Object>{
        let uri: string = "http://127.0.0.1:5000/auth/login";
        let data = new URLSearchParams();
        let body={
            "username": username,
            "password": passphrase
        };
        for (let key in body){
            data.append(key, body[key]);
        }
        return this._http.post(
            uri,data).map((response: Response) => <Object>response.json()
            )
        .catch(
            this.errorHandler
        )
    }

    registerUser(username: string, email: string, passphrase: string): Observable<Object>{
        let uri: string = "http://127.0.0.1:5000/auth/register";
        let data = new URLSearchParams();
        let body = {
            "username": username,
            "email": email,
            "password": passphrase
        }

        for (let key in body){
            data.append(key,body[key]);
        }

        return this._http.post(uri, data).map(
            (response: Response) => <Object>response.json()
        )
    }

    private errorHandler(error: Response){
        console.log(error);
        return Observable.throw(error.json())
    }
}
