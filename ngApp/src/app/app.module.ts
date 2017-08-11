import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AuthModule } from './auth/auth.module';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { AuthComponent } from './auth/auth.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
      BrowserModule, AuthModule,
      RouterModule.forRoot([
          {path: 'login', component: AuthComponent},
          {path: '', redirectTo: '/login', pathMatch: 'full'}
      ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
