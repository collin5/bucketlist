import { Injectable } from '@angular/core';
import { Http, Response, URLSearchParams, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/do';


@Injectable()
export class BucketlistService{

    constructor( private _http: Http ){}

    addBucket(title, desc): Observable<Object>{
        let $uri: string = "http://127.0.0.1:5000/bucketlists";
        let $data = new URLSearchParams();
        let $headers = new Headers();
        $headers.append('token', localStorage.getItem('token'));

        let $body = {
            "title": title,
            "description": desc
        };
        for (let key in $body){
            $data.append(key, $body[key]);
        }
        return this._http.post($uri, $data, {headers: $headers}).map(
            (response: Response) => <Object>response.json()
        ).catch(
            this.errorHandler
        )
    }

    private errorHandler(error: Response){
        console.log(error.json());
        return Observable.throw(error.json());
    }
}
