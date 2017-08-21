import { Injectable } from '@angular/core';
import { ActivatedRoute, Route, Router, CanActivate } from '@angular/router';


@Injectable()
export class BucketIdGuard implements CanActivate{
    constructor(private _route: ActivatedRoute, private _router: Router){
    }

    canActivate(){
        if(this._route.snapshot.params['id'] == undefined){
            this._router.navigate(['/dashboard']);
            return false;
        }
        return true;
    }
}

