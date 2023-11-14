import { Injectable } from '@angular/core';
import { httpManager } from './httpManager';
import { of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private httpManager: httpManager) {
   }

  search(searchString : string)
  {
    return this.httpManager.search(searchString);
  }
}
