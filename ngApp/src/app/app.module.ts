import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AuthModule } from './auth/auth.module';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { AuthComponent } from './auth/auth.component';
import { DashboardModule } from './dashboard/dashboard.module';
import { Dashboard } from './dashboard/dashboard.component';

import { AuthGuard } from './auth/auth-guard.service';

import { BucketInfoComponent } from './dashboard/bucket/bucket-info.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
      BrowserModule, AuthModule,
      DashboardModule,
      RouterModule.forRoot([
          { path: 'login', component: AuthComponent },
          { path: '', redirectTo: '/login', pathMatch: 'full' },
          { path: 'dashboard', component: Dashboard, canActivate: [
              AuthGuard
          ] },
          { path:'dashboard/bucket/:id', component: BucketInfoComponent, canActivate: [
              AuthGuard
          ] }
      ])
  ],
    providers: [
        AuthGuard
    ],
  bootstrap: [AppComponent]
})
export class AppModule { }
