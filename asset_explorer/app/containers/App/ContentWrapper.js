import styled from 'styled-components';

const ContentWrapper = styled.div`
  // as flex child of App
  -webkit-order: 0;
  -ms-flex-order: 0;
  order: 0;
  -webkit-flex: 1 1 auto;
  -ms-flex: 1 1 auto;
  flex: 1;
  -webkit-align-self: stretch;
  -ms-flex-item-align: stretch;
  align-self: stretch;

  // as flex parent of content section
  display: flex;
  flex-direction: column;
  overflow: auto;
`;

export default ContentWrapper;
