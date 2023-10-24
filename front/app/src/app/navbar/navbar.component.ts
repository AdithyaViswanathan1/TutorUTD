import { Component, Input, OnChanges, SimpleChanges } from "@angular/core";

@Component({
    selector: 'app-navbar',
    templateUrl: './navbar.component.html',
    styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnChanges{
    constructor() {
    }

    @Input() user: number = 0; //0 = not logged in, 1 = student, 2 = teacher
    
    ngOnChanges(changes: SimpleChanges): void {
    }
    
}