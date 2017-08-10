import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';

@Injectable()
export class AuthService{
    constructor( private _http: Http ){

    }
    getToken(username: string, passphrase: string): Observable<any>{
        let uri: string = "http://127.0.0.1:5000/auth/login";
        return this._http.post(uri,{
            username: username,
            password: passphrase
        }).map((response: Response) => <any>response.json()).catch(
            this.errorHandler
        )
    }

    private errorHandler(error: Response){
        console.log(error);
        return Observable.throw(error.json().error || 'Server Error')
    }
}
