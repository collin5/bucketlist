import { Component } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
    selector: 'app-login',
    moduleId: module.id,
    templateUrl: 'login.component.html'
})
export class LoginComponent {
    private error_msg: string = "";
    constructor(private _auth: AuthService){

    }

    onLogin(username, passphrase): void{
        this._auth.getToken(username, passphrase).subscribe(
            (data: any) => this.authenticate,
            error => this.error_msg = <any>error)
    }

    private authenticate(data){
        console.log(data)
    }
}
