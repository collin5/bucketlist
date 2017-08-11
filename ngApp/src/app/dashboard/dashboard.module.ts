import { NgModule } from '@angular/core';
import { Dashboard } from './dashboard.component';
import { SharedModule } from '../shared/shared.module';

@NgModule({
    declarations: [
        Dashboard
    ],
    imports: [
        SharedModule
    ],
    providers: []
})
export class DashboardModule{}

