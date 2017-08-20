import { Component, Input } from '@angular/core';

@Component({
    selector: 'app-bucket',
    moduleId: module.id,
    templateUrl: 'bucket.component.html'
})
export class Bucket{
    @Input() title: string;
    @Input() description: string;
}
