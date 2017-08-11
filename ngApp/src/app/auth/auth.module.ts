import { NgModule } from '@angular/core';
import { AuthComponent } from './auth.component';
import { AuthService } from './auth.service';
import { HttpModule } from '@angular/http';
import { SharedModule } from '../shared/shared.module';


@NgModule({
    declarations: [
        AuthComponent
    ],
    imports: [
        SharedModule
    ],
    providers: [
        AuthService
    ]
})
export class AuthModule{}
