import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable()
export class AuthGuard implements CanActivate{
    constructor(private _router: Router){}
    canActivate(){
        // redirect if token is not present
        if (!localStorage.token){
            this._router.navigate(['/login']);
            return false;
        }
        return true;
    }
}
